// ============================================
// GAME STATE
// ============================================
let xState = [0, 0, 0, 0, 0, 0, 0, 0, 0];
let oState = [0, 0, 0, 0, 0, 0, 0, 0, 0];
let turn = 1; // 1 for X, 0 for O
let gameActive = true;
let scores = {
    x: 0,
    o: 0,
    draws: 0
};

// Winning combinations (same as Python version)
const winningCombinations = [
    [0, 1, 2], // Top row
    [3, 4, 5], // Middle row
    [6, 7, 8], // Bottom row
    [0, 3, 6], // Left column
    [1, 4, 7], // Middle column
    [2, 5, 8], // Right column
    [0, 4, 8], // Diagonal top-left to bottom-right
    [2, 4, 6]  // Diagonal top-right to bottom-left
];

// ============================================
// DOM ELEMENTS
// ============================================
const cells = document.querySelectorAll('.cell');
const currentPlayerElement = document.getElementById('currentPlayer');
const playerMarkElement = document.getElementById('playerMark');
const gameStatusElement = document.getElementById('gameStatus');
const resetBtn = document.getElementById('resetBtn');
const victoryOverlay = document.getElementById('victoryOverlay');
const victoryText = document.getElementById('victoryText');
const playAgainBtn = document.getElementById('playAgainBtn');
const xScoreElement = document.getElementById('xScore');
const oScoreElement = document.getElementById('oScore');
const drawScoreElement = document.getElementById('drawScore');

// ============================================
// HELPER FUNCTIONS
// ============================================

// Sum function (from Python code)
function sum(a, b, c) {
    return a + b + c;
}

// Check for win condition (ported from Python)
function checkWin(xState, oState) {
    for (let win of winningCombinations) {
        // Check if X wins
        if (sum(xState[win[0]], xState[win[1]], xState[win[2]]) === 3) {
            return { winner: 'X', combination: win };
        }
        // Check if O wins
        if (sum(oState[win[0]], oState[win[1]], oState[win[2]]) === 3) {
            return { winner: 'O', combination: win };
        }
    }
    return null;
}

// Check for draw
function checkDraw() {
    // Game is a draw if all cells are filled and no winner
    return xState.every((val, idx) => val === 1 || oState[idx] === 1);
}

// Update player indicator
function updatePlayerIndicator() {
    const currentPlayer = turn === 1 ? 'X' : 'O';
    playerMarkElement.textContent = currentPlayer;
    playerMarkElement.className = 'player-mark ' + (turn === 1 ? 'x-turn' : 'o-turn');
}

// Update score display
function updateScoreDisplay() {
    xScoreElement.textContent = scores.x;
    oScoreElement.textContent = scores.o;
    drawScoreElement.textContent = scores.draws;
}

// Highlight winning cells
function highlightWinningCells(combination) {
    combination.forEach(index => {
        cells[index].classList.add('winning');
    });
}

// Show victory overlay
function showVictory(message) {
    victoryText.textContent = message;
    victoryOverlay.classList.add('show');
}

// Hide victory overlay
function hideVictory() {
    victoryOverlay.classList.remove('show');
}

// ============================================
// GAME LOGIC
// ============================================

function handleCellClick(event) {
    const cell = event.target;
    const index = parseInt(cell.dataset.index);

    // Prevent clicking on already taken cells or if game is over
    if (!gameActive || cell.classList.contains('taken')) {
        return;
    }

    // Mark the cell
    if (turn === 1) {
        xState[index] = 1;
        cell.textContent = 'X';
        cell.classList.add('x', 'taken');
    } else {
        oState[index] = 1;
        cell.textContent = 'O';
        cell.classList.add('o', 'taken');
    }

    // Check for win
    const winResult = checkWin(xState, oState);
    if (winResult) {
        gameActive = false;
        highlightWinningCells(winResult.combination);
        
        // Update scores
        if (winResult.winner === 'X') {
            scores.x++;
        } else {
            scores.o++;
        }
        updateScoreDisplay();
        
        // Show victory message
        setTimeout(() => {
            showVictory(`🎉 Player ${winResult.winner} Wins! 🎉`);
        }, 500);
        
        gameStatusElement.textContent = `Player ${winResult.winner} wins!`;
        return;
    }

    // Check for draw
    if (checkDraw()) {
        gameActive = false;
        scores.draws++;
        updateScoreDisplay();
        
        setTimeout(() => {
            showVictory(`🤝 It's a Draw! 🤝`);
        }, 500);
        
        gameStatusElement.textContent = "It's a draw!";
        return;
    }

    // Switch turns
    turn = 1 - turn;
    updatePlayerIndicator();
}

// Reset the game board (keep scores)
function resetGame() {
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    oState = [0, 0, 0, 0, 0, 0, 0, 0, 0];
    turn = 1;
    gameActive = true;
    
    cells.forEach(cell => {
        cell.textContent = '';
        cell.className = 'cell';
    });
    
    gameStatusElement.textContent = '';
    updatePlayerIndicator();
    hideVictory();
}

// ============================================
// EVENT LISTENERS
// ============================================

// Add click listeners to all cells
cells.forEach(cell => {
    cell.addEventListener('click', handleCellClick);
});

// Reset button
resetBtn.addEventListener('click', resetGame);

// Play again button (in victory overlay)
playAgainBtn.addEventListener('click', resetGame);

// ============================================
// INITIALIZATION
// ============================================

// Initialize the game
updatePlayerIndicator();
updateScoreDisplay();

// Add keyboard support for accessibility
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && victoryOverlay.classList.contains('show')) {
        resetGame();
    }
});

// Add touch support for mobile devices
cells.forEach(cell => {
    cell.addEventListener('touchstart', (e) => {
        e.preventDefault();
        handleCellClick(e);
    }, { passive: false });
});

console.log('🎮 Tic Tac Toe - Modern Edition loaded successfully!');
console.log('Enjoy the game! 🎉');

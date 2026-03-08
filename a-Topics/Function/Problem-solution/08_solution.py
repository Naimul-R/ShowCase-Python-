def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(Name="Iron-Man", Power="Leadership")
print_kwargs(Name="Hulk")
print_kwargs(Name="SpiderMan", Power="spider-net", enemy="Dr.octopus")
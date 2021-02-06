rivers={
    'Indus':['Tibet, Kashmir, and Pakistan'],
    'Rhine':['Switzerland, Germany, and The Netherlands'],
    'Volga':['Russia']
}
for key, value in rivers.items():
    if type(value)==list:
        print(f"The {\nkey.title()} river flows through:")
        for v in value:
            print("\t",v)
    else:
        print(f"The{key.title()} river flows through {value.title()}")

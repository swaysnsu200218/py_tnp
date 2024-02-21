def outer():
    name = "swayansu"
    def inner():
        nonlocal name
        print(name)
        name = "panda"
    inner()
    print(name)
outer()
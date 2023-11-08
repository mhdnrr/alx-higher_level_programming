import builtins
print(*getattr(builtins.__build_class__, "__subclasses__")()[66]()._doc.split()[2:28])

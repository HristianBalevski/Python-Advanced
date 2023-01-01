def func_executor(*args):
    result = []

    for func_reference, func_arguments in args:
        func_result = func_reference(*func_arguments)
        result.append(f"{func_reference.__name__} - {func_result}")
    return "\n".join(result)
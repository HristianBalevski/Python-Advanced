def concatenate(*args, **kwargs):
    final_text = ''.join(args)

    for key, value in kwargs.items():
        final_text = final_text.replace(key, value)
    return final_text


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
from contextlib import contextmanager


@contextmanager
def temporary_setting(settings, key, new_value):

    old_value = settings[key]

    settings[key] = new_value

    try:
        yield settings
    finally:
        settings[key] = old_value


app_settings = {
    "theme": "light",
    "language": "English"
}

print("Before:", app_settings)

with temporary_setting(app_settings, "theme", "dark"):
    print("Inside:", app_settings)

print("After:", app_settings)
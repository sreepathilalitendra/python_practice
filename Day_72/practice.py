
import subprocess
import sys

# Challenge 1: Display installed Python version
result = subprocess.run(
    [sys.executable, "--version"],
    capture_output=True,
    text=True
)

print("Python version:")
print(result.stdout or result.stderr)


# Challenge 2: Print your name using subprocess
result = subprocess.run(
    [
        sys.executable,
        "-c",
        "print('My name is Lalitendra')"
    ],
    capture_output=True,
    text=True
)

print("\nName:")
print(result.stdout)


# Challenge 3: Display return code
result = subprocess.run(
    [
        sys.executable,
        "-c",
        "print('Successful command')"
    ],
    capture_output=True,
    text=True
)

print("Return code:", result.returncode)


# Challenge 4: Capture standard output
result = subprocess.run(
    [
        sys.executable,
        "-c",
        "print('This is standard output')"
    ],
    capture_output=True,
    text=True
)

print("\nStandard output:")
print(result.stdout)


# Challenge 5: Capture standard error
result = subprocess.run(
    [
        sys.executable,
        "-c",
        "import sys; print('Sample error message', file=sys.stderr)"
    ],
    capture_output=True,
    text=True
)

print("\nStandard error:")
print(result.stderr)


# Challenge 6: Run a Python calculation
result = subprocess.run(
    [
        sys.executable,
        "-c",
        "print('Addition:', 25 + 15)"
    ],
    capture_output=True,
    text=True
)

print("\nCalculation:")
print(result.stdout)


# Challenge 7: Pass your name as input
result = subprocess.run(
    [
        sys.executable,
        "-c",
        "name = input(); print('Welcome', name)"
    ],
    input="Lalitendra",
    capture_output=True,
    text=True
)

print("\nInput result:")
print(result.stdout)


# Challenge 8: Use check=True
try:
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "print('Task completed successfully')"
        ],
        capture_output=True,
        text=True,
        check=True
    )

    print("\nCheck result:")
    print(result.stdout)

except subprocess.CalledProcessError as error:
    print("Command failed:", error)


# Challenge 9: Display CompletedProcess information
result = subprocess.run(
    [
        sys.executable,
        "-c",
        "print('CompletedProcess example')"
    ],
    capture_output=True,
    text=True
)

print("\nCompletedProcess details:")
print("Arguments:", result.args)
print("Return code:", result.returncode)
print("Output:", result.stdout)


# Challenge 10: Simple Python Script Runner
script_path = "sample_script.py"

with open(script_path, "w", encoding="utf-8") as file:
    file.write(
        "print('Hello from Script Runner!')\n"
        "print('Python script executed successfully')\n"
    )

result = subprocess.run(
    [sys.executable, script_path],
    capture_output=True,
    text=True
)

print("\nPython Script Runner")

if result.returncode == 0:
    print("Script executed successfully")
    print("Output:")
    print(result.stdout)
else:
    print("Script execution failed")
    print(result.stderr)

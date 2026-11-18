
import subprocess
import sys

# Example 1: Run a simple command
result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print("Python version:")
print(result.stdout or result.stderr)


# Example 2: Check return code
result = subprocess.run(
    ["python", "--version"],
    capture_output=True,
    text=True
)

print("\nReturn code:", result.returncode)


# Example 3: Capture command output
result = subprocess.run(
    [sys.executable, "-c", "print('Hello from subprocess!')"],
    capture_output=True,
    text=True
)

print("\nOutput:")
print(result.stdout)


# Example 4: Check errors
result = subprocess.run(
    [sys.executable, "-c", "print('Program executed successfully')"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Program completed successfully")
else:
    print("Program failed")


# Example 5: Capture standard error
result = subprocess.run(
    [
        sys.executable,
        "-c",
        "import sys; print('Sample error', file=sys.stderr)"
    ],
    capture_output=True,
    text=True
)

print("\nStandard error:")
print(result.stderr)


# Example 6: Run another Python script
script = """
print("This is another Python script")
print("Executed using subprocess")
"""

result = subprocess.run(
    [sys.executable, "-c", script],
    capture_output=True,
    text=True
)

print("\nAnother script output:")
print(result.stdout)


# Example 7: Use input with subprocess
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

print("\nInput example:")
print(result.stdout)


# Example 8: Use check=True
try:
    result = subprocess.run(
        [sys.executable, "-c", "print('Task successful')"],
        capture_output=True,
        text=True,
        check=True
    )

    print("\nCheck result:")
    print(result.stdout)

except subprocess.CalledProcessError as error:
    print("Command failed:", error)


# Example 9: CompletedProcess information
result = subprocess.run(
    [sys.executable, "-c", "print('Python subprocess')"],
    capture_output=True,
    text=True
)

print("\nCompletedProcess information:")
print("Arguments:", result.args)
print("Return code:", result.returncode)
print("Output:", result.stdout)


# Example 10: Run a system command
result = subprocess.run(
    ["cmd", "/c", "echo Hello from Windows"],
    capture_output=True,
    text=True
)

print("\nWindows command output:")
print(result.stdout)

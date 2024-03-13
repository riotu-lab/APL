# python_runner.py
import tempfile
import subprocess

class PythonRunner:
    def run_code(self, py_code: str):
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(py_code)
            temp_file_name = temp_file.name

        try:
            # Run the code and get output
            process = subprocess.Popen(['python', temp_file_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            output = stdout.decode().strip()
            error = stderr.decode().strip()

            if error:
                return f"Error: {error}"
            else:
                return output
        finally:
            # Delete the temporary file
            subprocess.run(['rm', temp_file_name])

# Example usage:

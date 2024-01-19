# Use the official Microsoft PowerShell image
FROM mcr.microsoft.com/powershell

# Set the working directory inside the container
WORKDIR /scripts

# Copy the PowerShell script into the container
COPY RE1.ps1 .

# Run the PowerShell script when the container starts
CMD ["pwsh", "./RE1.ps1"]

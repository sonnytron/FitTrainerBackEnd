# FitTrainerBackEnd

This will be a Django back-end for my Android/iOS Fitness application

### Setup Instructions  
  
  1. Pull down the repository using HTTP or SSH.  
  2. If you haven't done so already, inside your home directory create a /.config folder with a folder titled "FitTrainer" inside of it. On Mac's this final directory would be "/Users/{UserName}/.config/FitTrainer/".  
  3. Run "echo 1 > ~/.config/FitTrainer/DEBUG" in Terminal.
  4. Change directories into the root folder of FitTrainerBackEnd/.  
  5. Install a virtualenv using "virtualenv -p python3 {virtualEnvName}  
  6. Run your virtual environment using "source {virtualEnvName}/bin/activate".  
  7. You should see the {virtualEnvName} in your terminal appended to the beginning or end of your console line.  
  8. Run "pip install -e ." to install dependencies.  
  9. Finally, run "fittrainer runserver" in order to deploy the development environment on your local machine.

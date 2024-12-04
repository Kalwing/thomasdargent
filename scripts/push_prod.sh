#!/bin/zsh
CSUCCESS="\033[1;92m"
CINFO="\033[0;36m"
CERROR="\033[0;31m"
CDEBUG="\033[0;30m"
RESET="\033[0m"

log_status() {
    echo -e "${CINFO}- $1${RESET}"
}

handle_error() {
    echo -e "${CERROR}Error: $1${RESET}"
    exit 1
}

deploy() {
    log_status "Uploading dist..."
    echo "${CDEBUG}"
    scp -r dist kalwing:~/thomasdargent || handle_error "Failed to upload dist directory"
    scp -r flask_app kalwing:~/thomasdargent || handle_error "Failed to upload flask directory"

    log_status "Cleaning previous deployment..."
    ssh kalwing 'rm -rf /var/www/thomasdargent/dist' || handle_error "Failed to delete the dist folder"
    ssh kalwing 'rm -rf /var/www/thomasdargent/flask_app' || handle_error "Failed to delete the flask folder"

    log_status "Moving the files to the prod directory..."
    ssh kalwing 'mv ~/thomasdargent/dist /var/www/thomasdargent' || handle_error "Failed to move dist"
    ssh kalwing 'mv ~/thomasdargent/flask_app /var/www/thomasdargent' || handle_error "Failed to move flask_app"

    log_status "Asking service to restart..."
    ssh kalwing 'echo \"Last update: $(date +%F-%T)\" > /var/www/thomasdargent/.update' || handle_error "Failed to trigger update"

    echo "-${CSUCCESS} ✓ Deployment successful!${RESET}"
}

deploy
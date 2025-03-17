#!/bin/bash

artifact_name="flask-response-job-1"
max_attempts=5
attempt=1

echo "Esperando el artifact $artifact_name..."

while [ $attempt -le $max_attempts ]; do
  echo "Intentando descargar artifact... intento $attempt/$max_attempts"
  if ! artifact=$(gh run download-artifact --name "$artifact_name" --repo "$GITHUB_REPOSITORY" 2>/dev/null); then
    echo "Artifact no disponible aún, esperando..."
    sleep 10
  else
    echo "Artifact descargado exitosamente"
    mv "$artifact_name"/* .
    break
  fi
  ((attempt++))
done

if [ ! -f "flask_response.txt" ]; then
  echo "No se pudo descargar el artifact después de $max_attempts intentos"
  exit 1
fi
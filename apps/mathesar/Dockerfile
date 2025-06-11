# Renovate can update the MATESAR_IMAGE_TAG argument.
ARG MATESAR_IMAGE_TAG=0.1.7
FROM mathesar/mathesar:${MATESAR_IMAGE_TAG} AS base_mathesar

# --- STAGE: Build with S3 and OIDC Dependencies and Custom Settings ---
# This stage adds django-storages, boto3, python-oidc-client, and your custom settings
FROM base_mathesar AS custom_base_mathesar

WORKDIR /code/mathesar

# Install additional Python dependencies for S3 storage and OIDC
# These are added to the environment provided by Mathesar's base image.
COPY custom-requirements.txt .
RUN pip install --no-cache-dir -r custom-requirements.txt \
    && rm custom-requirements.txt

# Copy custom Django setting to Mathesar settings directory
COPY custom_settings.py config/settings/custom_settings.py

# Set the default settings module for the runtime.
# This will be overridden by Kubernetes environment variables for flexibility.
ENV DJANGO_SETTINGS_MODULE=config.settings.custom_settings

# --- FINAL STAGE: Production S3/OIDC Image ---
# This stage uses the build stage's output for the final slim image
FROM base_mathesar AS custom_production
# Copy the modified application code (with S3 and OIDC packages and custom settings)
# from the mathesar_ stage into the final image.
COPY --from=custom_base_mathesar /code/mathesar /code/mathesar

WORKDIR /code/mathesar
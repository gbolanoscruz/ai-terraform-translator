import pytest
from app import detect_provider

def test_detect_provider_azure():
    codigo_terraform = 'provider "azurerm" {\n  features {}\n}'
    assert detect_provider(codigo_terraform) == "Azure"

def test_detect_provider_aws():
    codigo_terraform = 'provider "aws" {\n  region = "us-east-1"\n}'
    assert detect_provider(codigo_terraform) == "AWS"

def test_detect_provider_gcp():
    codigo_terraform = 'provider "google" {\n  project = "mi-proyecto"\n}'
    assert detect_provider(codigo_terraform) == "GCP"

def test_detect_provider_desconocido():
    codigo_terraform = 'provider "oci" {\n  region = "us-ashburn-1"\n}'
    assert detect_provider(codigo_terraform) == "Desconocido"
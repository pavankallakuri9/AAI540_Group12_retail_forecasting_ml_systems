import boto3
import sagemaker

# -----------------------------------
# AWS Session Setup
# -----------------------------------

session = boto3.session.Session()
region = session.region_name

sagemaker_session = sagemaker.Session()
default_bucket = sagemaker_session.default_bucket()

# -----------------------------------
# Project Info
# -----------------------------------

#PROJECT_NAME = "retail_forecasting"
DATABASE_NAME = "retail_forecasting"

REGION = region

# -----------------------------------
# S3 Data Lake Structure
# -----------------------------------

BUCKET = "retail-demand-forecasting-datalake"

RAW_DATA_PREFIX = "raw/corporacion_favorita"
PROCESSED_DATA_PREFIX = "processed/corporacion_favorita"
ATHENA_STAGING_PREFIX = "athena/staging"

# -----------------------------------
# S3 Paths
# -----------------------------------

S3_RAW_PATH = f"s3://{BUCKET}/{RAW_DATA_PREFIX}/"
S3_PROCESSED_PATH = f"s3://{BUCKET}/{PROCESSED_DATA_PREFIX}/"
S3_STAGING_DIR = f"s3://{BUCKET}/{ATHENA_STAGING_PREFIX}/"

# -----------------------------------
# Individual Dataset Paths
# -----------------------------------

S3_TRAIN_PATH = f"{S3_RAW_PATH}train/train.csv"
S3_STORES_PATH = f"{S3_RAW_PATH}stores/stores.csv"
S3_TRANSACTIONS_PATH = f"{S3_RAW_PATH}transactions/transactions.csv"
S3_OIL_PATH = f"{S3_RAW_PATH}oil/oil.csv"
S3_HOLIDAYS_PATH = f"{S3_RAW_PATH}holidays/holidays_events.csv"


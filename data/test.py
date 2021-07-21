import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, request
import pandas as pd
#################################################
# Database Setup
#################################################
# Create an engine that allo us to to communicate with the database
from config import password
engine = create_engine(f'postgresql+psycopg2://postgres:{password}@localhost:5432/project_olympics')


print(engine.tables)
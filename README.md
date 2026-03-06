# Record Management System

## Overview
This repository contains a group project dedicated to designing a robust record management system for a specialist travel agent. The programme features a Graphical User Interface (GUI) and allows users to efficiently manage three distinct types of records: Client records, Flight records, and Airline Company records.

## Core Features
Through the Graphical User Interface, the user is able to perform the following operations:
- **Create** a new record
- **Delete** an existing record
- **Update** a record's details
- **Search and Display** specific records

## Technical Specifications

### Data Storage
- **Internal Memory:** During execution, records are held in memory as a list of dictionaries (e.g., `records: list = [{}, {}]`).
- **Persistent Storage:** Data is saved to the local file system using either binary format (Pickle), JSON, or JSONL (JSON lines). 
- **Lifecycle:** The application automatically verifies the existence of previous records upon startup and loads them. All changes are saved back to the file system when the application is closed.

### Record Formats
The system manages three primary data structures:

#### 1. Client Record
- **ID:** `int`
- **Type:** `str` (type of record)
- **Name:** `str`
- **Address Line 1:** `str`
- **Address Line 2:** `str`
- **Address Line 3:** `str`
- **City:** `str`
- **State:** `str`
- **Zip Code:** `str`
- **Country:** `str`
- **Phone Number:** `str`

#### 2. Airline Record
- **ID:** `int`
- **Type:** `str` (type of record)
- **Company Name:** `str`

#### 3. Flight Record
- **Client_ID:** `int`
- **Airline_ID:** `int`
- **Date:** `date/time`
- **Start City:** `str`
- **End City:** `str`

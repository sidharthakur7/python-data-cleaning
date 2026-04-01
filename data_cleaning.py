{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0b69e31d-dbf7-4639-acd2-9c1259eb9bd6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Origina Data:\n",
      "    Name   Age  Salary\n",
      "0   John  25.0   50000\n",
      "1    NaN  30.0   60000\n",
      "2   John  25.0   50000\n",
      "3  Alice   NaN   70000\n",
      "4    Bob  28.0   55000\n",
      "\n",
      "Cleaned Data:\n",
      "\n",
      "Shape Before Cleaning\n",
      "Shape After Cleaning (4, 3)\n",
      "    name   age  salary\n",
      "0   John  25.0   50000\n",
      "1    NaN  30.0   60000\n",
      "3  Alice   NaN   70000\n",
      "4    Bob  28.0   55000\n",
      "\n",
      "Data Cleaned Sucessfully!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "\n",
    "#Load Data\n",
    "df= pd.read_csv(\"data.csv\")\n",
    "\n",
    "\n",
    "print(\"Origina Data:\")\n",
    "print(df)\n",
    "\n",
    "#Remove rows with missing values \n",
    "df.dropna()\n",
    "\n",
    "#Remove Duplicate roes to avoid repeated data\n",
    "df=df.drop_duplicates()\n",
    "\n",
    "#Stanardize column names (remove spaces and lowercase)\n",
    "df.columns=df.columns.str.strip().str.lower()\n",
    "\n",
    "#Save Cleaned Data\n",
    "df.to_csv(\"cleaned_data.csv\",index=False)\n",
    "\n",
    "print(\"\\nCleaned Data:\")\n",
    "print(\"\\nShape Before Cleaning\")\n",
    "print(\"Shape After Cleaning\",df.shape)\n",
    "print(df)\n",
    "\n",
    "print(\"\\nData Cleaned Sucessfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52da830a-fafd-4639-8774-ba4fd6285998",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

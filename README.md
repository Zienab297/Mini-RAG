# Mini-RAG

Implementing a simple RAG tutorial

## installation

### Install required packages 
```bash
$ pip install -r requiremnets
```
### Setup the environment variables

``` bash
$ cp .env.example .env
```
Don't forget to setup your variables in the `.env` file
1.  `OPENAI_API_KEY` value

## Run the FastAPI Server 

```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

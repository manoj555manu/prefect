from prefect import  flow

@flow(log_prints=True)
def first():
    print("Hello !")

if __name__ == "__main__":
    first()

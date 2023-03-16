# Loan Prediction using Machine Learning,ETL(using pyspark) and Big Data Technologies
## Snapshots of the deployment on EC2 instance
![alt insert](https://github.com/ShreyasK2411/Loan_Prediction/blob/fe422b0b1aad9ea190658fa73c46951c50dee0a1/images/snapshot1.png?raw=true)
![alt insert](https://github.com/ShreyasK2411/Loan_Prediction/blob/30c425cdeb41051a1fd3c38f19d6e9d4b44ea24a/images/snapshot2.png?raw=true)
# *steps for running the project*
## Step 1: Commands for setting up docker and git
```bash
sudo yum install -y docker
```
```bash
sudo yum install -y git
```
```bash
sudo systemctl start docker
```
```bash
git clone https://github.com/ShreyasK2411/Loan_Prediction.git
```

## Step 2: Setting up HBase
*Note: copy the setup file to home directory and run the script in sudo mode and copy the last line of the file to the systems /etc/hosts.
```bash
docker exec -it hbase-docker cat /etc/hosts
```
```bash
echo hbase-docker <IP> >> /etc/hosts
```

## Step 3: Download the data
```bash
mkdir .kaggle
```
```bash
mv /home/ec2-user/Loan_Prediction/kaggle.json .kaggle
```
```bash
chmod 777 .kaggle/kaggle.json
```
- go to /dev/ and download the dataset
- change the permissions of the folder
- exit the sudo mode and then download the data
```bash
kaggle datasets download -d mrmorj/alfabattle-20
```
```bash
sudo unzip alfabattle-20.zip -d /run
```

## Step 4: Insert the data in HBase
```bash
sudo python3 toHBase.py
```
- Enter the following after prompt
  - column family name = details
  - file path = /run/alfabattle2_train_transactions_contest/train_transactions_contest

## Step 5: Build the Website Docker image
```bash
sudo docker build . -t webserver
```
```bash
sudo docker exec -it webserver echo <IP> >> /etc/hosts
```
```bash
docker run -p 8767:8767 --name website -d webserver
```

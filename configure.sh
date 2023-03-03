# sudo yum install git

# git clone https://github.com/ShreyasK2411/Loan_Prediction.git

mkdir /home/hadoop/.kaggle
mv Loan_Prediction/kaggle.json /home/hadoop/.kaggle

sudo pip3 install kaggle
sudo pip3 install pyspark

sudo yum install python3-devel
sudo pip3 install happybase

cd /emr/
kaggle datasets download -d mrmorj/alfabattle-20

sudo unzip alfabattle-20.zip -d /run


# /run/alfabattle2_train_transactions_contest/train_transactions_contest




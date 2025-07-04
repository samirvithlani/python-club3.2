from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (classification_report,confusion_matrix,roc_auc_score,log_loss)

data ={
    'text':[
        "the client agrees to pay payment fee",
    "payment must be made within 10 days",
    "either party may terminate",
    "all disputes shall be resolved under the laws of the jurisdiction",
    "the service provider shall maintain confidentiality of client data",
    "failure to comply with these terms may result in immediate termination",
    "both parties agree to act in good faith",
    "any amendment to this agreement must be in writing and signed by both parties",
    "the agreement shall commence on the effective date and continue until terminated",
    "neither party shall be liable for delays caused by force majeure events"
    ],
    'label':[
       "payment",
         "payment",
         "termination",
            "jurisdiction",
        "confidentiality",
        "termination",
        "good faith",
        "amendment",
        "commencement",
        "force majeure"  
    ]
}

df = pd.DataFrame(data)

#vectorization
vectorizer = TfidfVectorizer(stop_words='english')
x =  vectorizer.fit_transform(df['text'])
y = df['label']


#train model
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(classification_report(y_test,y_pred))


def predict_clause(text):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]


exmaples = ["the buyer shall payment within 15 days","the agreement may be terminated by either party","all propritery data must be kept confidential",""]

for ex in exmaples:
    print(f"ex : {ex} {predict_clause(ex)}")

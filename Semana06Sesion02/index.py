from flask import Flask
import router
app = Flask(__name__)

@app.get("/")

def index():
    data = router.probar()
    
        users = [('id':1,'name':'juan')]
    return "Hola mundo!!"
if __name__ == "__main__":

    app.run(host="127.0.0.1", port=4000)
    
    ##get: obtener
    ##post: INsertar
    ## put: actualziar datos
    ## delete: eliminar
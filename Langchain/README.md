    
# Langchain + Groq Tutorial

Ce projet est un tutoriel complet pour apprendre à utiliser [Langchain](https://www.langchain.com/) avec l'API [Groq](https://console.groq.com/), en tant qu'alternative gratuite à OpenAI/Claude. Vous apprendrez à :

- Créer des modèles de prompts dynamiques
- Générer des prédictions avec LLaMA 3
- Obtenir des sorties structurées via Pydantic
- Créer des chaînes complexes et des agents intelligents

---

## 📦 Installation

Installez les dépendances nécessaires avec :

```bash
pip install langchain langchain-groq pydantic
```

---

## 🔑 Configuration de l'API Groq

1. Créez un compte sur [https://console.groq.com](https://console.groq.com)
2. Générez une clé API
3. Ajoutez-la dans vos variables d’environnement :

```bash
export GROQ_API_KEY='votre_cle_api'
```

Ou directement dans votre code :

```python
import os
os.environ["GROQ_API_KEY"] = "votre_cle_api"
```

---

## 🤖 Utilisation

### 1. Génération simple de texte

```python
from langchain_groq import ChatGroq

llm = ChatGroq(model="llama3-70b-8192", temperature=0.3, max_tokens=500)
response = llm.invoke("Quels sont les 7 merveilles du monde ?")
print(response.content)
```

### 2. Modèle de prompt avec `PromptTemplate`

```python
from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "Liste {n} plats typiques de la cuisine {cuisine}."
)
prompt = prompt_template.format(n=3, cuisine="italienne")
response = llm.invoke(prompt)
print(response.content)
```

### 3. Sortie structurée avec Pydantic

```python
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser

class Movie(BaseModel):
    title: str = Field(description="Titre du film")
    genre: list[str] = Field(description="Genres du film")
    year: int = Field(description="Année de sortie")

parser = PydanticOutputParser(pydantic_object=Movie)
prompt = prompt_template.format(query="Un film des années 90 avec Nicolas Cage.")
response = llm.invoke(prompt)
parsed = parser.parse(response.content)
print(parsed)
```

### 4. Création d’un Agent IA

Un agent IA peut utiliser plusieurs outils pour résoudre un problème complexe. Vous pouvez connecter des APIs externes, des bases de connaissances ou des fonctions Python personnalisées.

> Cette section nécessite une configuration plus avancée. Voir [la doc officielle](https://python.langchain.com/docs/modules/agents/) pour plus d'exemples.

---

## 🧠 Fonctionnalités supplémentaires

- **RAG (Retrieval-Augmented Generation)** : permet à un LLM d’accéder à des documents ou données externes
- **Mémoire** : pour permettre à l’agent de se souvenir des conversations passées
- **LangChain Expression Language (LCEL)** : nouvelle syntaxe puissante pour enchaîner prompts, modèles et parsers

---

## 📄 Licence

Ce projet est distribué sous licence MIT.

    

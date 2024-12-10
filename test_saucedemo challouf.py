from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialiser le driver
driver = webdriver.Chrome()  # Assurez-vous que ChromeDriver est dans votre PATH

try:
    # Étape 1 : Accéder à la page d'accueil
    driver.get("https://www.saucedemo.com/")
    print("Navigué vers le site SauceDemo.")

    # Étape 2 : Vérifier que le titre de la page est correct
    time.sleep(2)  # Attendre quelques secondes pour s'assurer que la page se charge
    assert "Swag Labs" in driver.title, "Erreur : La page d'accueil ne s'est pas chargée correctement."
    print("Test réussi : La page d'accueil s'est chargée avec succès.")

    # Étape 3 : Vérifier que le bouton de connexion est visible
    login_button = driver.find_element(By.ID, "login-button")
    assert login_button.is_displayed(), "Erreur : Le bouton de connexion n'est pas visible."
    print("Test réussi : Le bouton de connexion est visible sur la page d'accueil.")

except AssertionError as error:
    # Afficher l'erreur en cas de test échoué
    print(f"Test échoué : {error}")

except Exception as e:
    # Gestion d'autres erreurs
    print(f"Une erreur inattendue s'est produite : {e}")

finally:
    # Étape 4 : Fermer le navigateur
    driver.quit()
    print("Navigateur fermé.")

import kaggle

kaggle.api.authenticate() # Para poder utilizar esta funcion debes crear un api key de kaggle y guardarlo en la carpeta .kaggle en tu home directory
kaggle.api.dataset_download_files('dhrubangtalukdar/e-commerce-shopper-behavior-amazonshopify-based', path='.', unzip=True) #e_comerce
kaggle.api.dataset_download_files('ahsan81/food-ordering-and-delivery-app-dataset', path='.', unzip=True) #COMIDA
kaggle.api.dataset_download_files("aminasalamt/social-media-dataset-2025", path='.', unzip=True) #social_media
import sys

from google.api_core.client_options import ClientOptions
from google.cloud import automl_v1
from google.cloud.automl_v1.proto import service_pb2

def inline_text_payload(file_path):
  with open(file_path, 'rb') as ff:
    content = ff.read()
  return {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }

def pdf_payload(file_path):
  return {'document': {'input_config': {'gcs_source': {'input_uris': [file_path] } } } }

def get_prediction(file_path, model_name):
  options = ClientOptions(api_endpoint='automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  payload = inline_text_payload(file_path)
  # Uncomment the following line (and comment the above line) if want to predict on PDFs.
  # payload = pdf_payload(file_path)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned

def get_prediction_text(content, model_name):
  options = ClientOptions(api_endpoint='automl.googleapis.com')
  prediction_client = automl_v1.PredictionServiceClient(client_options=options)

  payload = {'text_snippet': {'content': content, 'mime_type': 'text/plain'} }
  # Uncomment the following line (and comment the above line) if want to predict on PDFs.
  # payload = pdf_payload(file_path)

  params = {}
  request = prediction_client.predict(model_name, payload, params)
  return request  # waits until request is returned

if __name__ == '__main__':
#   file_path = sys.argv[1]
#   model_name = sys.argv[2]
    file_path = "dacon/target.txt"
    model_name = "projects/724413311684/locations/us-central1/models/TCN7180158375051657216"

# response = get_prediction(file_path, model_name)

# response = get_prediction_text("고객님", model_name)
# print("Prediction results:")
# for result in response.payload:
#     print("Predicted class name: {}".format(result.display_name))
#     print("Predicted class score: {}".format(result.classification.score))
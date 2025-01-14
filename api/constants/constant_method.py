from rest_framework_simplejwt.tokens import AccessToken
from django.conf import settings
import os, json
APP_CONSTANT_PATH = 'api/constants'
EU_FILE = 'en.json'

PENDING = 'Pending'
MEASUREMENT_DONE = 'Measurement Done'
QUOTATION_SENT = 'Quotation sent'
RESCEDULE = 'Re-Schedule'
REJECTED = 'Rejected'
CALLBACKREQUESTED = 'Call Back Requested'
ACCEPTED = 'Accepted'

INTERIOR_PAINTING = 'Interior Painting'
EXTERIOR_PAINTING = 'Exterior Painting'
WATERPROOFING = 'Waterproofing'
OTHER = 'OTHER'

ONEBHK = '1 BHK'
TWOBHK = '2 BHK'
THREEBHK = '3 BHK'
ROWHOUSE = 'Row House'
INDEPENDENTVILLA = 'Independent Villa'

def read_json_file(path=APP_CONSTANT_PATH,fileName=EU_FILE):
    try:
        file_path = os.path.join(settings.BASE_DIR, path, fileName)
        with open(file_path,"r") as file:
            file_data = json.loads(file.read())
            return file_data
    except Exception as e:
        return {}


def get_userId_from_access_token(request):
    token = request.headers['Authorization']
    if str(token).startswith('Bearer '):
        token = str(token).split(' ')[1]
        access_token = AccessToken(token)
        return access_token['user_id']
    return None

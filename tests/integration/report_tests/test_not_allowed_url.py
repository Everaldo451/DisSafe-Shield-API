import logging
from flask.testing import FlaskClient

def test_not_allowed_url(client:FlaskClient, url_prefix, succesReportData, createTokenRow):

    url = "http://youtube.com"
    succesReportData["proof"] = url

    response = client.post(f"{url_prefix}/report",
                                    
        json = succesReportData,
        headers = {
            "Authorization": f"Bearer {createTokenRow}"
        }
    )
    json = response.get_json()
    res = json["message"]
    assert res == 'Report was completed successfully, but some links were not included.'
    assert response.status_code == 400

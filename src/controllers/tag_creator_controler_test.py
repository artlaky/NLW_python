from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controler import TagCreatorControler

@patch.object(BarcodeHandler, 'creta_barcode')
def test_create(mock_creat_barcode):
    mock_value = "image_path"
    mock_creat_barcode.return_value = mock_value
    tag_creator_controler = TagCreatorControler()

    result = tag_creator_controler.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"]
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag Image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f'{mock_value}.png'

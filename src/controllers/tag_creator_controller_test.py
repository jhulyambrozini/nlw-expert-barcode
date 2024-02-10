from unittest.mock import patch
from src.drivers.barcode_handle import BarcodeHandle
from .tag_creator_controller import TagCreatorController

@patch.object(BarcodeHandle, 'create_barcode')
def test_create(mock_creator_barcode):
    mock_value = "image_path"
    mock_creator_barcode.return_value = mock_value
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result['data']
    assert "count" in result['data']
    assert "path" in result['data']

    assert result['data']['type'] == "Tag image"
    assert result['data']['count'] == 1
    assert result['data']['path'] == f'{mock_value}.png'

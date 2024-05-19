from pdf2image import convert_from_bytes
import io
import zipfile

class PDFToImageConverter:

    _static_image_format_to_extension_map = {
    "PNG": "png",
    "JPEG": "jpg"
    }

    def __init__(self, pdf_name, pdf_bytes):
        self.pdf_name = pdf_name
        self.pdf_bytes = pdf_bytes

    def _convert_to_images(self):
        return convert_from_bytes(self.pdf_bytes)

    def export_as_zip(self, image_format):
        images = self._convert_to_images()
        zip_buffer = io.BytesIO()

        with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED) as zip_file:
            for i, image in enumerate(images):
                image_data = io.BytesIO()
                image.save(image_data, format=image_format)  # Change format as needed
                zip_file.writestr(f"{self.pdf_name}_page_{i+1}." + self._static_image_format_to_extension_map[image_format], image_data.getvalue())

        zip_data = zip_buffer.getvalue()

        return zip_data
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import PDFFile


def list_files(request):
    files = PDFFile.objects.all()
    data = [
        {
            "name": file.file.name.split("/")[-1],
            "thumbnail": file.thumbnail.url if file.thumbnail else None,
        }
        for file in files
    ]
    return JsonResponse(data, safe=False)


def download_file(request, filename):
    file = get_object_or_404(PDFFile, file=f"pdfs/{filename}")
    return FileResponse(file.file, as_attachment=True)


@csrf_exempt
def upload_file(request):
    if request.method == "POST" and request.FILES["file"]:
        pdf_file = request.FILES["file"]
        new_file = PDFFile(file=pdf_file)
        new_file.save()
        return JsonResponse({"status": "success", "filename": new_file.file.name})
    return JsonResponse({"status": "fail"}, status=400)

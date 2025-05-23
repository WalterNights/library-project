import { NgIf } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-bulk-upload-books',
  standalone : true,
  imports: [NgIf, FormsModule],
  templateUrl: './bulk-upload-books.component.html',
})
export class BulkUploadBooksComponent {
  selectedFile: File | null = null;
  message: string = '';

  constructor(private http: HttpClient) { }
  onFileChange(event: any) {
    this.selectedFile = event.target.files[0];
  }

  onSubmit() {
    if (!this.selectedFile) {
      console.log('No file selected');
      return;
    }
    console.log('File selected:', this.selectedFile);

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post('http://localhost:8000/api/books/bulk_upload/', formData).subscribe({
      next: (res: any) => {
        this.message = res.message || 'Carga exitosa.';
      },
      error: err => this.message = err.error?.error || 'Error en la carga.'
    });
  }
}
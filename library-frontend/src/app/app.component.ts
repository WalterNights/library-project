import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { BulkUploadBooksComponent } from './bulk-upload-books/bulk-upload-books.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet, BulkUploadBooksComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  standalone: true,
})
export class AppComponent {
  title = 'library-frontend';
}

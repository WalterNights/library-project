import { Router } from '@angular/router';
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../environments/environment';

@Component({
  selector: 'app-books-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './books-list.component.html',
  styleUrls: ['./books-list.component.css']
})
export class BooksListComponent {
  books: any[] = [];

  constructor(private http: HttpClient, private router: Router) {}

  ngOnInit() {
    this.http.get<any[]>(`${environment.apiUrl}/books/`).subscribe({
      next: (data) => {
        this.books = data;
      },
      error: (error) => {
        console.error('Error fetching books:', error);
      }
    });
  }

  viewDetails(bookId: number) {
    this.router.navigate([`${environment.apiUrl}/books/`, bookId]);
  }
}

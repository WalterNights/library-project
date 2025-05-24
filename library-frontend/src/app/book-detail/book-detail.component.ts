import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-book-detail',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './book-detail.component.html',
  styleUrls: ['./book-detail.component.css'],
})
export class BookDetailComponent implements OnInit {
  book: any;
  user: any;
  hasBook = false;

  constructor(private http: HttpClient, private route: ActivatedRoute) { }

  ngOnInit(): void {
    const bookId = this.route.snapshot.paramMap.get('id');
    this.http.get(`/api/books/${bookId}/`).subscribe(book => {
      this.book = book;
    });

    const userId = typeof window !== 'undefined' ? localStorage.getItem('user_id') : null;
    if (!userId) {
      return;
    }
    const token = localStorage.getItem('access_token');
    this.http.get('/api/users/me/', {
      headers: { Authorization: `Bearer ${token}` }
    }).subscribe((user: any) => {
      this.user = user;
      this.hasBook = user.borrowed_book.includes(Number(bookId));
    });
  }

  lend_book() {
    const token = localStorage.getItem('access_token');
    this.http.post(`api/books/${this.book.id}/lend/`, {},
      {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe(() => {
        this.hasBook = true;
      });
  }

  return_book() {
    const token = localStorage.getItem('access_token');
    this.http.post(`api/books/${this.book.id}/return/`, {},
      {
        headers: { Authorization: `Bearer ${token}` }
      }).subscribe(() => {
        this.hasBook = false;
      });
  }
}

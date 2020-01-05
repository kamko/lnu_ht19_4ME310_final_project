import { Injectable } from '@angular/core';
import { HttpService } from './http-service.service';
import { Observable } from 'rxjs';

export interface Page<T> {
  items: T[];
  page: number;
  hasNext: boolean;
  hasPrev: boolean;
  pages: number;
  perPage: number;
  total: number;
}

@Injectable({
  providedIn: 'root'
})
export class ArticleService {

  constructor(private http: HttpService) { }

  public fetchArticle(id: number) {
    return this.http.get(
      `/article/${id}`) as Observable<Article>;
  }

  public fetchPage(page: number) {
    if (page === null || page === undefined) {
      page = 1;
    }

    return this.http.get(
      `/article?page=${page}`) as Observable<Page<Article>>;
  }
}

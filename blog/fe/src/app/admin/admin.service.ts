import { Injectable } from '@angular/core';
import { HttpService } from '../http-service.service';
import { Observable } from 'rxjs';
import { Page } from '../article.service';

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  constructor(private http: HttpService) { }

  public fetchArticle(id: number) {
    return this.http.get(
      `/admin/article/${id}`) as Observable<AdminArticle>;
  }

  public page(page: number) {
    return this.http.get(
      `/admin/article?page=${page}`) as Observable<Page<AdminArticle>>;
  }

  public publish(id: number) {
    return this.http.put(
      `/admin/article/${id}/publish`, {}) as Observable<AdminArticle>;
  }

  public unpublish(id: number) {
    return this.http.put(
      `/admin/article/${id}/unpublish`, {}) as Observable<AdminArticle>;
  }

  public create(cmd: ArticleCreateCmd): Observable<AdminArticle> {
    return this.http.post(
      '/admin/article', cmd) as Observable<AdminArticle>;
  }

  public update(id: number, cmd: ArticleCreateCmd): Observable<AdminArticle> {
    return this.http.put(
      `/admin/article/${id}`, cmd) as Observable<AdminArticle>;
  }
}

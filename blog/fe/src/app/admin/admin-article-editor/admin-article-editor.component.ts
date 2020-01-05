import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';
import { Observable, of } from 'rxjs';
import { map, switchMap } from 'rxjs/operators';
import { ActivatedRoute, Router } from '@angular/router';
import { AdminService } from '../admin.service';

@Component({
  selector: 'app-admin-article-editor',
  templateUrl: './admin-article-editor.component.html',
  styleUrls: ['./admin-article-editor.component.css']
})
export class AdminArticleEditorComponent implements OnInit {

  private static placeholder: AdminArticle = {
    id: 0,
    title: '',
    content: '',
    publishedAt: undefined,
    createdAt: undefined,
    isPublished: undefined,
    popularityLevel: undefined
  };


  public data$: Observable<AdminArticle>;

  constructor(
    private readonly route: ActivatedRoute,
    private readonly router: Router,
    private readonly service: AdminService,
    private location: Location
  ) {
    route.params.subscribe(_ => {
      this.data$ = this.route.paramMap.pipe(
        map(paramMap => paramMap.get('id')),
        map(id => +id),
        switchMap(id =>
          (id === 0)
            ? of(Object.assign({}, AdminArticleEditorComponent.placeholder))
            : this.service.fetchArticle(id)
        )
      );
    });
  }

  ngOnInit() { }

  public saveArticle(article: AdminArticle) {
    const cmd = {
      title: article.title,
      content: article.content
    };

    let response;
    if (article.id === 0) {
      response = this.service.create(cmd);
    } else {
      response = this.service.update(article.id, cmd);
    }

    response.subscribe(art => {
      this.router.navigate(['/', 'admin', 'article', art.id]);
    });
  }

  returnBack() {
    this.router.navigate(['/', 'admin', 'articles']);
  }
}

import { Component, OnInit, ViewChild, ChangeDetectorRef } from '@angular/core';
import { Location } from '@angular/common';
import { PageEvent, MatPaginator, MatTableDataSource } from '@angular/material';
import { ActivatedRoute } from '@angular/router';
import { AdminService } from '../admin.service';
import { map } from 'rxjs/operators';

@Component({
  selector: 'app-admin-article-list',
  templateUrl: './admin-article-list.component.html',
  styleUrls: ['./admin-article-list.component.css']
})
export class AdminArticleListComponent implements OnInit {

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
  public dataSource: MatTableDataSource<AdminArticle>;
  displayedColumns: string[] = ['id', 'title', 'createdAt', 'publishedAt', 'isPublished', 'popularity', 'actions'];

  pageEvent: PageEvent;

  constructor(
    private readonly route: ActivatedRoute,
    private service: AdminService,
    private location: Location
  ) { }

  populateDataSource(page: number) {
    this.service.page(page).subscribe(
      p => {
        this.dataSource.data = p.items;
        this.paginator.length = p.total;
        this.paginator.pageSize = p.perPage;
        this.location.go(`admin/articles/${p.page}`);
      }
    );
  }

  ngOnInit() {
    this.dataSource = new MatTableDataSource();

    this.route.params.subscribe(_ => {
      this.route.paramMap.pipe(
        map(paramMap => paramMap.get('page')),
        map(page => +page),
      ).subscribe(page => {
        this.populateDataSource(page);
        this.paginator.pageIndex = page - 1;
      });
    });
  }

  handleEvent(event: PageEvent) {
    this.populateDataSource(event.pageIndex + 1);
  }

  unpublish(article: AdminArticle) {
    this.service.unpublish(article.id)
      .subscribe(updated => this.refreshDataSource(updated));
  }

  publish(article: AdminArticle) {
    this.service.publish(article.id)
      .subscribe(updated => this.refreshDataSource(updated));
  }

  private refreshDataSource(updated: AdminArticle) {
    const idx = this.dataSource.data.findIndex(i => i.id === updated.id);
    this.dataSource.data[idx] = updated;
    this.dataSource.data = [...this.dataSource.data];
  }
}

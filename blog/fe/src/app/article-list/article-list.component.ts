import { Component, OnInit, ViewChild } from '@angular/core';
import { Location } from '@angular/common';
import { ArticleService } from '../article.service';
import { ActivatedRoute } from '@angular/router';
import { map } from 'rxjs/operators';
import { MatTableDataSource, MatPaginator, PageEvent } from '@angular/material';

@Component({
  selector: 'app-article-list',
  templateUrl: './article-list.component.html',
  styleUrls: ['./article-list.component.css']
})
export class ArticleListComponent implements OnInit {

  @ViewChild(MatPaginator, { static: true }) paginator: MatPaginator;
  public dataSource: MatTableDataSource<Article>;
  displayedColumns: string[] = ['data'];

  pageEvent: PageEvent;

  constructor(
    private readonly route: ActivatedRoute,
    private service: ArticleService,
    private location: Location
  ) { }

  populateDataSource(page: number) {
    this.service.fetchPage(page).subscribe(
      p => {
        this.dataSource.data = p.items;
        this.paginator.length = p.total;
        this.paginator.pageSize = p.perPage;
        this.location.go(`articles/${p.page}`);
      }
    );
  }

  handleEvent(event: PageEvent) {
    this.populateDataSource(event.pageIndex + 1);
  }

  ngOnInit() {
    this.dataSource = new MatTableDataSource();

    this.route.params.subscribe(_ => {
      this.route.paramMap.pipe(
        map(paramMap => paramMap.get('page')),
        map(page => +page),
      ).subscribe(page => this.populateDataSource(page));
    });
  }

}

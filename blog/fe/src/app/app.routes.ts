import { Routes } from '@angular/router';
import { AdminArticleEditorComponent } from './admin/admin-article-editor/admin-article-editor.component';
import { ArticleListComponent } from './article-list/article-list.component';
import { AdminArticleListComponent } from './admin/admin-article-list/admin-article-list.component';

export const routes: Routes = [
    { path: '', redirectTo: 'articles/1', pathMatch: 'full' },
    { path: 'articles/:page', component: ArticleListComponent },
    { path: 'admin/articles', redirectTo: 'admin/articles/1', pathMatch: 'full' },
    { path: 'admin/articles/:page', component: AdminArticleListComponent },
    { path: 'admin/article/:id', component: AdminArticleEditorComponent },
];

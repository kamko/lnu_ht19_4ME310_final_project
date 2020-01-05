interface AdminArticle {
    id: number;
    title: string;
    content: string;
    publishedAt: Date;
    createdAt: Date;
    isPublished: boolean;
    popularityLevel: number;
}

interface ArticleCreateCmd {
    title: string;
    content: string;
}
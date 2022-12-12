import { Component, OnInit } from '@angular/core';
import { Article } from 'src/app/entities/article.model';
import { Post } from 'src/app/entities/post.model';
import { TextExtract } from 'src/app/entities/text-extract.model';
import { AdminService } from 'src/app/services/admin.service';
import { ArticleService } from 'src/app/services/article.service';
import { TextService } from 'src/app/services/text.service';

@Component({
  selector: 'all-history',
  templateUrl: './all-history.component.html',
  styleUrls: ['./all-history.component.css']
})
export class AllHistoryComponent implements OnInit {
  public articles: Article[] = [];
  public articleTweets: Post[] = [];
  public texts: TextExtract[] = [];
  public textTweets: Post[] = [];

  public displayArticles: boolean = true;
  public displayArticleTweets: boolean = true;
  public displayTextsTweets: boolean = true;
  public displayTexts: boolean = true;

  constructor(private articleService: ArticleService, private textService: TextService) { }

  ngOnInit(): void {
  }

  deleteArticle(id: number, index: number) {
    this.articleService.deleteArticle(id).subscribe();
    this.getAllArticles();
  }


  deleteText(id: number, index: number) {
    this.textService.deleteText(id).subscribe();
    this.getAllTexts();
  }

  getAllArticles()
  {
    this.articleService.getAllArticles()
      .subscribe((articles) =>
      {
        this.articles = articles;
      }
      )
  }

  getArticleTweets(article_id: number)
  {
    this.articleService.getArticlePosts(article_id)
    .subscribe((tweets) =>
    {
      this.articleTweets = tweets;
    });
  }

  getAllTexts()
  {
    this.textService.getAllTextExtracts()
      .subscribe((texts) =>
      {
        this.texts = texts;
      }
      )
  }

  getTextExtractsTweets(text_extract_id: number)
  {
    this.textService.getTextExtractsPosts(text_extract_id)
    .subscribe((tweets) =>
    {
      this.textTweets = tweets;
    });
  }

  searchArticleByTitle(title: string): void {
    this.articleService.getArticleByTitle(title)
    .subscribe((articles) =>
    {
      this.articles = articles;
    })
  }

  searchTextByTitle(title: string): void {
    this.textService.getTextByTitle(title)
    .subscribe((texts) =>
    {
      this.texts = texts;
    })
  }

}

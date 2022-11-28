import { Component, OnInit } from '@angular/core';
import { Article } from 'src/app/entities/article.model';
import { Post } from 'src/app/entities/post.model';
import { TextExtract } from 'src/app/entities/text-extract.model';
import { ArticleService } from 'src/app/services/article.service';
import { TextService } from 'src/app/services/text.service';

@Component({
  selector: 'app-history',
  templateUrl: './history.component.html',
  styleUrls: ['./history.component.css']
})
export class HistoryComponent implements OnInit {
  public articles: Article[] = [];
  public articleTweets: Post[] = [];
  public texts: TextExtract[] = [];
  public textTweets: Post[] = [];

  displayArticles: boolean = true;
  displayTexts: boolean = true;

  displayArticleTweets: boolean = true;
  displayTextsTweets: boolean = true;

  constructor(private textService: TextService, private articleService: ArticleService) { }

  ngOnInit(): void {
  }



  getArticles()
  {
    this.articleService.getArticles()
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

  getTexts()
  {
    this.textService.getTextExtracts()
      .subscribe((texts) =>
      {
        this.texts = texts;
        console.log(this.texts)
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



}

FROM ruby:2.7.2

WORKDIR /usr/src/app/docs

COPY docs/Gemfile ./
RUN bundle install

CMD bundle exec jekyll server --host=0.0.0.0

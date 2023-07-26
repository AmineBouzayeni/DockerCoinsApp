# Choose 3.2.2 as it is the last stable version.
FROM ruby:3.2.2-alpine3.18

RUN apk update && apk add --no-cache build-base

COPY Gemfile Gemfile.lock ./

RUN bundle install

COPY hasher.rb .

CMD ["ruby", "./hasher.rb"]
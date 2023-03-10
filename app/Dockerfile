FROM fhsinchy/php-nginx-base:php8.1.3-fpm-nginx1.20.2-alpine3.15

# set composer related environment variables
ENV PATH="/composer/vendor/bin:$PATH" \
    COMPOSER_ALLOW_SUPERUSER=1 \
    COMPOSER_VENDOR_DIR=/var/www/vendor \
    COMPOSER_HOME=/composer

# install composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \ && composer --ansi --version --no-interaction

# install application dependencies
WORKDIR /var/www/app
COPY ./src/composer.json ./src/composer.lock* ./
RUN composer install --no-scripts --no-autoloader --ansi --no-interaction

RUN apk add --update nodejs npm
COPY ./src/package.json ./src/package-lock.json /var/www/app/
RUN npm install

# add custom php-fpm pool settings, these get written at entrypoint startup
ENV FPM_PM_MAX_CHILDREN=20 \
    FPM_PM_START_SERVERS=2 \
    FPM_PM_MIN_SPARE_SERVERS=1 \
    FPM_PM_MAX_SPARE_SERVERS=3

# set application environment variables
ENV APP_NAME="laravel ben hassoun" \
    APP_ENV=production \
    APP_DEBUG=false

# copy entrypoint files
COPY ./docker/docker-php-* /usr/local/bin/
RUN dos2unix /usr/local/bin/docker-php-entrypoint
RUN dos2unix /usr/local/bin/docker-php-entrypoint-dev


# copy nginx configuration
COPY ./docker/nginx.conf /etc/nginx/nginx.conf
COPY ./docker/default.conf /etc/nginx/conf.d/default.conf

RUN chmod -R 777 /usr/local/bin/docker-php-entrypoint-dev
RUN chmod -R 777 /usr/local/bin/docker-php-entrypoint

COPY ./src/.env /var/www/app

RUN php artisan key:generate

# copy application code
WORKDIR /var/www/app
COPY ./src .
RUN chown -R www-data:www-data /var/www

RUN composer dump-autoload -o \
    && chown -R :www-data /var/www/app \
    && chmod -R 777 /var/www/app/storage /var/www/app/bootstrap/cache

EXPOSE 80

# run supervisor
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]

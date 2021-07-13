# Generated by Django 2.1.3 on 2019-04-23 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import seaimport.helpers.file_helper


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seaexport', '0001_initial'),
        ('freightman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeaImportAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(max_length=200)),
                ('postal_code', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('mobile', models.CharField(blank=True, max_length=30, null=True)),
                ('fax', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='freightman.City')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportAgentBankInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_no', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('swift_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bank_address', models.TextField(blank=True, null=True)),
                ('company', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportAgent')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.FileField(blank=True, null=True, upload_to='seaimport/agent/logo')),
                ('icon', models.FileField(blank=True, null=True, upload_to='seaimport/agent/icon')),
                ('is_forwarder', models.BooleanField(blank=True, default=False)),
                ('is_consignor', models.BooleanField(blank=True, default=False, verbose_name='Consignor')),
                ('is_importer', models.BooleanField(blank=True, default=True, verbose_name='Importer')),
                ('is_bank', models.BooleanField(blank=True, default=False, verbose_name='Bank')),
                ('is_foreign_agent', models.BooleanField(blank=True, default=False, verbose_name='Foreign Agent')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Country Name')),
                ('alpha2_code', models.CharField(max_length=2, unique=True, verbose_name='Alpha2 Code')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportCreditNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportAgent')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportCreditNoteCosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('credit_note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportCreditNote')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportDeliveryOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=100, verbose_name='To')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('cargo_system', models.CharField(max_length=200, verbose_name='Cargo System')),
                ('vessel', models.CharField(max_length=200, verbose_name='Vessel Name/Number')),
                ('line_no', models.CharField(max_length=30, verbose_name='Line No')),
                ('rotation_no', models.CharField(max_length=50, verbose_name='Import Rotation No')),
                ('lc_number', models.CharField(max_length=200, verbose_name='LC Number and Dated')),
                ('applicant_name', models.CharField(max_length=200, verbose_name='Applicants Name')),
                ('applicant_address', models.CharField(max_length=300, verbose_name='Applicants Address')),
                ('lcaf_number', models.CharField(max_length=200, verbose_name='LCAF NO.')),
                ('applicant_irc', models.CharField(max_length=200, verbose_name="Applicant's IRC No")),
                ('tin', models.CharField(max_length=200, verbose_name="Applicant's Tin No")),
                ('bin_no', models.CharField(max_length=200, verbose_name="Applicant's Bin No")),
                ('others', models.TextField(blank=True, null=True, verbose_name='Other Information')),
                ('bank_statement', models.FileField(blank=True, null=True, upload_to=seaimport.helpers.file_helper.bank_statement_documents, verbose_name='ATTACH SCANNED COPY OF BANK RELEASE')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='freightman.City')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportDoc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=seaimport.helpers.file_helper.job_documents_path_rename)),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportDocType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20, unique=True, verbose_name='Name of Document')),
                ('type_description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportExpense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportExpenseType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('default', models.FloatField(blank=True, default=0, null=True, verbose_name='Default Cost (USD)')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportFormInstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbl_form', models.TextField(blank=True, default='Please fill up the form to create and MBL document and attach the scanned copy of your mbl')),
                ('goods_form', models.TextField(blank=True, default='To add mode option click the blue + button beside fields. After adding please refresh the page to see the new option')),
                ('mbl_other_info_form', models.TextField(blank=True, default='To add mode option click the blue + button beside fields. After adding please refresh the page to see the new option')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportFreightType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('freight_certificate', models.BooleanField(blank=True, default=False, verbose_name='Requires Freight Certificate')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportGood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, default='AS PER INVOICE', null=True, verbose_name='Description')),
                ('container_seal_number', models.CharField(max_length=50, null=True, verbose_name='Container/Seal Number')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
                ('net_weight', models.FloatField(verbose_name='Net Weight')),
                ('gross_weight', models.FloatField(verbose_name='Gross Weight')),
                ('weight_unit', models.CharField(blank=True, default='KG', max_length=20, verbose_name='Container Size and Type')),
                ('container_size_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='container_type', to='seaexport.ContainerType', verbose_name='Container Type')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportGoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_type_name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('goods_type_description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportHbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hbl_number', models.CharField(default='', max_length=30, unique=True, verbose_name='HBL Number')),
                ('file', models.FileField(upload_to=seaimport.helpers.file_helper.hbl_documents_path_rename, verbose_name='ATTACH SCANNED COPY OF HBL DOCUMENT')),
                ('unlocked', models.BooleanField(blank=True, default=True)),
                ('hbl_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HBLBank', to='seaimport.SeaImportAgent', verbose_name='BANK')),
                ('hbl_consignor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HBLConsignor', to='seaimport.SeaImportAgent', verbose_name='CONSIGNOR')),
                ('hbl_notifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='HBLNotifier', to='seaimport.SeaImportAgent', verbose_name='NOTIFIER')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dollar_rate', models.FloatField(default=83, verbose_name='Current Dollar Rate')),
                ('job_costing_done', models.BooleanField(blank=True, default=False)),
                ('public_key', models.CharField(blank=True, editable=False, max_length=20, null=True, unique=True, verbose_name='JOB ID')),
                ('unlocked', models.BooleanField(blank=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportJobCost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('type', models.CharField(choices=[('1', 'Fixed Cost'), ('2', 'Per HBLS'), ('3', 'Per KG (New Weight)'), ('4', 'On CBM')], default='1', max_length=2)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportJob')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportJobCostType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('default', models.FloatField(blank=True, default=0, null=True, verbose_name='Default Cost (USD)')),
                ('type', models.CharField(choices=[('-1', 'Expense'), ('1', 'Income')], default='-1', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportMbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mbl_number', models.CharField(default='', max_length=30, verbose_name='MBL Number')),
                ('file', models.FileField(upload_to=seaimport.helpers.file_helper.mbl_documents_path_rename, verbose_name='ATTACH SCANNED COPY OF MBL DOCUMENT')),
                ('proforma_invoice_no', models.CharField(max_length=100, null=True, verbose_name='Proforma Invoice No.')),
                ('proforma_invoice_date', models.DateField(null=True, verbose_name='Proforma Invoice Date')),
                ('feeder_vessel', models.CharField(max_length=200, null=True, verbose_name='Feeder Vessel.')),
                ('eta_destination_port', models.DateField(null=True, verbose_name='Estimated Time of Arrival: DEST Port')),
                ('ocean_freight_cost_per_container', models.FloatField(null=True, verbose_name='Ocean Freight Charge Per Container (USD)')),
                ('unlocked', models.BooleanField(blank=True, default=True)),
                ('freight_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seaimport.SeaImportFreightType')),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='seaimport.SeaImportJob')),
                ('mbl_consignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MBLConsignee', to='seaimport.SeaImportAgent', verbose_name='CONSIGNEE')),
                ('mbl_notifier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MBLNotifier', to='seaimport.SeaImportAgent', verbose_name='NOTIFIER')),
                ('mbl_shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MBLShipper', to='seaimport.SeaImportAgent', verbose_name='CONSIGNOR')),
                ('port_of_discharge', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Destination_port', to='seaexport.SeaPort', verbose_name='Port of destination.')),
                ('port_of_loading', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Loading_port', to='seaexport.SeaPort', verbose_name='Port of loading.')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportCountry')),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportSystemSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_instruction', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('instructions', models.ForeignKey(default=1, editable=False, null=True, on_delete=models.SET(1), to='seaimport.SeaImportFormInstruction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeaImportTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_alert', models.BooleanField(blank=True, default=True)),
                ('forwarding_letter_issued', models.BooleanField(blank=True, default=False)),
                ('hbl_mbl_confirmation', models.BooleanField(blank=True, default=False)),
                ('igm', models.BooleanField(blank=True, default=False)),
                ('bin_number', models.BooleanField(blank=True, default=False)),
                ('invoice', models.BooleanField(blank=True, default=False)),
                ('freight_certificate', models.BooleanField(blank=True, default=True)),
                ('do_issued', models.BooleanField(blank=True, default=False)),
                ('unlocked', models.BooleanField(blank=True, default=True)),
            ],
        ),
        migrations.AddField(
            model_name='seaimportjobcost',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportJobCostType', verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='seaimportjob',
            name='task',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportTask'),
        ),
        migrations.AddField(
            model_name='seaimporthbl',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='seaimport.SeaImportJob'),
        ),
        migrations.AddField(
            model_name='seaimporthbl',
            name='task',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportTask'),
        ),
        migrations.AddField(
            model_name='seaimportgood',
            name='hbl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportHbl'),
        ),
        migrations.AddField(
            model_name='seaimportgood',
            name='mbl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportMbl'),
        ),
        migrations.AddField(
            model_name='seaimportgood',
            name='package_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='package_type', to='seaexport.SeaExportPackageType', verbose_name='Package Type'),
        ),
        migrations.AddField(
            model_name='seaimportgood',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportGoodType', verbose_name='Goods Type'),
        ),
        migrations.AddField(
            model_name='seaimportexpense',
            name='hbl',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportHbl'),
        ),
        migrations.AddField(
            model_name='seaimportexpense',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportExpenseType'),
        ),
        migrations.AddField(
            model_name='seaimportdoc',
            name='doc_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='seaimport.SeaImportDocType'),
        ),
        migrations.AddField(
            model_name='seaimportdoc',
            name='job',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportJob'),
        ),
        migrations.AddField(
            model_name='seaimportdeliveryorder',
            name='hbl',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportHbl'),
        ),
        migrations.AddField(
            model_name='seaimportcreditnotecosts',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportJobCostType', verbose_name='Cost Type'),
        ),
        migrations.AddField(
            model_name='seaimportcreditnote',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportJob'),
        ),
        migrations.AddField(
            model_name='seaimportagent',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seaimport.SeaImportCompany', verbose_name='Company'),
        ),
        migrations.AlterUniqueTogether(
            name='seaimportagent',
            unique_together={('name', 'branch')},
        ),
    ]